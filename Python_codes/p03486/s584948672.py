s = sorted(list(input()))
t = sorted(list(input()))[::-1]
            
for S, T in zip(s, t):
    if S < T:
        print('Yes')
        exit()
    elif S > T:
        print('No')
        exit()
    else:
        continue

print('Yes' if len(s) < len(t) else 'No')