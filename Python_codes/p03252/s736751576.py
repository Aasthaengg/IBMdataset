s = list(input())
t = list(input())
s_to_t = {chr(c):set() for c in range(ord('a'),ord('z')+1)}
t_to_s = {chr(c):set() for c in range(ord('a'),ord('z')+1)}

for i in range(len(s)):
    s_to_t[s[i]].add(t[i])
    t_to_s[t[i]].add(s[i])

for c in range(ord('a'), ord('z')+1):
    if len(s_to_t[chr(c)]) > 1 or len(t_to_s[chr(c)]) > 1:
        print('No')
        exit()
print('Yes')