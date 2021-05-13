S = input()
size = len(S)
patterns = []
ans = 0

def flagfun(flag):
    if len(flag) == size:
        patterns.append(flag+"1")
        return
    
    flagfun(flag+'0')
    flagfun(flag+'1')

flagfun('')

for pattern in patterns:
    lastKey = 0
    for k, v in enumerate(pattern):
        if v == "1":
            if len(S[lastKey:k]) != 0:
                ans += int(S[lastKey:k])
                lastKey = k

print(int(ans/2))