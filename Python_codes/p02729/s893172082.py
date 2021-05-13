n, m = map(int, input().split())
nAns= (((n+1)*n)/2)-n
mAns= (((m+1)*m)/2)-m
print(int(nAns+mAns))