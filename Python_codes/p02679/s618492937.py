import math
import copy

def main():
    N=int(input())
    zero_fish=0

    Pair={}

    for i in range(N):
        A,B=map(int,input().split())

        if A==0 and B==0:
            zero_fish+=1
            continue
        if B==0:
            bunsi=1
            bunbo=0
        elif B>0:
            bunsi=A//math.gcd(A,B)
            bunbo=B//math.gcd(A,B)
        else:
            bunsi=-1*A//math.gcd(A,B)
            bunbo=-1*B//math.gcd(A,B)

        key = str(bunsi) + "/" + str(bunbo)

        if bunsi == 0 or bunbo == 0:
            rev_bunsi = bunbo
            rev_bunbo = bunsi
        elif bunsi < 0:
            rev_bunsi = bunbo
            rev_bunbo = -1 * bunsi
        else:
            rev_bunsi = -1 * bunbo
            rev_bunbo = bunsi
        rev_key = str(rev_bunsi) + "/" + str(rev_bunbo)

        if (key in Pair.keys()):
            Pair[key][0]+=1
        elif (rev_key in Pair.keys()):
            Pair[rev_key][1]+=1
        else:
            Pair[key]=[1,0]

    res=1
    mod=1000000007
    for p in Pair.values():
        if p[1]==0:
            temp=pow(2,p[0],mod)
        else:
            temp=(pow(2,p[0],mod)+pow(2,p[1],mod)-1)%mod
        res=(res*temp)%mod
    res+=zero_fish-1

    print(res%mod)

if __name__=="__main__":
    main()
