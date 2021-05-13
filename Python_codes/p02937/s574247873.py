from collections import defaultdict
import bisect
def main():
    s = list(input())
    t = list(input())
    dic_s = defaultdict(list)
    for i in range(len(s)):
        dic_s[s[i]].append(i)
    x,y = 0,-1
    for i in range(len(t)):
        if dic_s[t[i]] == []:
            print(-1)
            return
        next_y = bisect.bisect_left(dic_s[t[i]],y+1)
        if next_y == len(dic_s[t[i]]):
            x += 1
            y = dic_s[t[i]][0]
        else:
            y = dic_s[t[i]][next_y]
    print(x*len(s)+y+1)

if __name__ == "__main__":
    main()