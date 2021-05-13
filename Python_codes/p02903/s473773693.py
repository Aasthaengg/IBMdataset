H,W,A,B=map(int,input().split())
ans=[['0']*W for _ in range(H)]
for a in range(B):
    ans[a][:A]=['1']*A
for a in range(B,H):
    ans[a][A:]=['1']*(W-A)
for a in ans:
    print(''.join(a))