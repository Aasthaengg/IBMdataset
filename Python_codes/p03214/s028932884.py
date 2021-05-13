n = int(input())
frame = list(map(int, input().split()))
avg = sum(frame) / n
ans= []
for d in frame:
    ans.append(abs(d-avg)) 
    
print(ans.index(min(ans)))
