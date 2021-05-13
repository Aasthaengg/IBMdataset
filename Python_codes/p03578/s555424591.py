def f():
    n=int(input())
    from collections import Counter as co
    p=co(list(map(int,input().split())))
    m=int(input())
    q=co(list(map(int,input().split())))
    for k in q:
        if k not in p or p[k]<q[k]:
            print("NO");break
    else:print("YES")
if __name__ == "__main__":
    f()