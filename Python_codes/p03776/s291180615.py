import itertools,collections
import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
def main():
    n,a,b=map(int, input().split())
    v=[int(i) for i in input().split()]
    v.sort(reverse = True)
    tmp = v[0:a]
    dd = collections.defaultdict(int)

    for i in v:
        dd[i]+=1

    cnt = 0
  
    k = 0
    for i in tmp:
        k+=i
    s = min(tmp)
    avg = k/len(tmp)
    if(tmp[0]!=s):
        howmany = v.count(s)
        nantoori = tmp.count(s)
        #howmany個からnantoori個選ぶ方法
        res = howmany

        for i in range(nantoori-1):
            res *= (howmany-i+1)
        res2 = 1
        for i in range(nantoori):
            res2 *= (i+1)
        print(avg)
        print(combinations_count(howmany,nantoori))
    else:
        howmany = dd[s]
        res=0
        for i in range(a,min(b+1,howmany+1)):
            res += combinations_count(howmany, i)


        print(avg)
        print(res)


if __name__ == '__main__':
    main()
