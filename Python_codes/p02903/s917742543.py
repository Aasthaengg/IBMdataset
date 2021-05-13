H,W,A,B=map(int,input().split())
print(*['0'*A+'1'*(W-A) if i<B else '1'*A+'0'*(W-A) for i in range(H)],sep='\n')