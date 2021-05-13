from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n,m=map(int,readline().split())
    d=make_divisors(m)
    l=m//n
    for v in d:
        if v<=l:
            print(v)
            break

def make_divisors(n):
    if n==1:
        divisors=[1]
        return divisors
    else:
        divisors=[]
        for i in range(1,n):
            if i*i>n:
                break
            if n%i==0:
                divisors.append(i)
                if i!=n//i:
                    divisors.append(n//i)

        divisors.sort(reverse=True)
        return divisors

if __name__=="__main__":
    main()