from sys import stdin
from itertools import permutations
def main():
    #入力
    readline=stdin.readline
    li=[int(readline()) for _ in range(5)]

    ans=float("inf")
    for i in permutations(li):
        tmp=0
        for j in range(5):
            if j!=4:
                if i[j]%10==0:
                    tmp+=i[j]
                else:
                    tmp+=i[j]+10-i[j]%10
            else:
                tmp+=i[j]

        ans=min(ans,tmp)

    print(ans)

if __name__=="__main__":
    main()