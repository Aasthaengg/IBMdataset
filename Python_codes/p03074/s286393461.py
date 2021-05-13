N, K = map(int, input().split())
S = input()
ts = []

s1 = 0
s0 = 0

if N < K:
    print(N)
    exit(0)
# Create 01 array
for c in S:
    if c == '1':
        s1 += 1
        if not s0 == 0:
            ts.append((0, s0))
        s0 = 0
    else:
        s0 += 1
        if not s1 == 0:
            ts.append((1,s1))
        s1 = 0

if s1 != 0:
    ts.append((1,s1))
if s0 != 0:
    ts.append((0,s0))

# print("TS:", ts)

# top/bottom
top0 = False
bottom0 = False

if ts[0][0] == 0:
    top0 = True

if ts[-1][0] == 0:
    bottom0 = True

# print(top0, bottom0)
## pre calc
if len(ts) >= 2:
    ans = 1
else:
    ans = ts[0][1]
# print(ans)

sp = 0
ep = len(ts)

if top0:
    ans = sum(x[1] for x in ts[:K*2])
    # print("t0:", ans)
    sp = 1

if bottom0:
    ans = max(ans, sum(x[1] for x in ts[-K*2:]))
    # print("b0:", ans)
    ep = len(ts)-1

# Calc
# print(sp, ep)
if ep - sp > 1:
    W = 2 * K + 1
    temp = sum([x[1] for x in ts[sp:sp+W]])
    # print("temp:", temp)
    ans = max(temp, ans)

    for ix in range(sp+2, ep-W+1, 2):
        temp = temp - ts[ix-1][1] - ts[ix-2][1] + ts[ix+W-1][1] + ts[ix+W-2][1]
        # print(ix, temp)
        ans = max(temp, ans)

print(ans)