N,K = list(map(int,input().split()))
V = list(map(int,input().split()))
out = 0
for left in range(0,K+1):
    for right in range(0,K-left+1):
        if left==0 and right==0:
            continue
        if left + right <= N:
            if right!=0:
                box = V[0:left] + V[N-right:N]
            else:
                box = V[0:left]
            S = sum(box)
            box.sort(reverse=True)
            t = -1
            Life = K-(left+right)
            while Life>0 and abs(t)<=len(box) and box[t]<0:
                S = S-box[t]
                Life += -1
                t += -1
            if S>out:
                out = S
print(max(out,0))