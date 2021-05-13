N = int(input())

S = []

for _ in range(N):
    S.append(input())


# internal ab count
internal_ab = 0
for s in S:
    for i in range(1,len(s)):
        if s[i-1] == 'A' and s[i] == 'B':
            internal_ab += 1

# edge
a_pool = 0
b_pool = 0
ab_pool = 0
edge_ab = 0
for s in S:
    if s[0] == 'B' and s[-1] == 'A':
        ab_pool += 1 
    elif s[0] == 'B':
        b_pool += 1
    elif s[-1] == 'A':
        a_pool += 1

if ab_pool == 0:
    edge_ab = min(a_pool, b_pool)
elif a_pool + b_pool == 0:
    edge_ab = ab_pool - 1
else:
    edge_ab = ab_pool + min(a_pool, b_pool)
    
print(internal_ab+edge_ab)