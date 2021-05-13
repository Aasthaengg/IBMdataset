N,A,B=map(int,input().split())
ans=(A+B*(N-1))-(A*(N-1)+B)+1
print(ans if ans>=0 else 0)