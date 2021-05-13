a,b=map(int,input().split())
c=list(input())
c=c[:b-1]+[c[b-1].swapcase()]+c[b:]
print("".join(c))