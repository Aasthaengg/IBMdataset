import math
import collections
def main():
    n = int(input())
    s = []
    dd = collections.defaultdict(int)
    for i in range(n):
        a  = int(input())
        dd[a]+=1
        s.append(a)
    k = max(dd.keys())
    lis = sorted(list(dd.keys()),reverse = True)

    for i in range(n):
        if(s[i]==k and dd[s[i]]==1):
            print(lis[1])
        else:
            print(k)






if __name__ == '__main__':
    main()
