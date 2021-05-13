def main():
    K=int(input())
    A=list(map(int,input().split()))
    A.reverse()
    minres = 2
    maxres = 2
    for a in A:
        minres = ((minres+a-1)//a)*a
        if minres>maxres:return -1
        maxres = (maxres//a)*a+a-1
    return str(minres)+" "+str(maxres)

print(main())