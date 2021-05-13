
url = "https://atcoder.jp//contests/abc061/tasks/abc061_c"
import heapq


def main():
    n,k = list(map(int, input().split()))
    dic = {}
    for _ in range(n):
        t = list(map(int, input().split()))
        dic.setdefault(t[0], 0)
        dic[t[0]] += t[1]
    dic_sorted = sorted(dic.items(), key=lambda x: x[0])
    count = 0
    for l in dic_sorted:
        count += l[1]
        if count >= k:
            print(l[0])
            exit()



if __name__ == '__main__':
    main()
