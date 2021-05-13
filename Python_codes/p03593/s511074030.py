from collections import Counter

H, W = map(int, input().split())
s = ''
for _ in range(H):
    s += input()
jdg = True
cnt = Counter(s)
lst = list(cnt.values())
lst4 = [l%4 for l in lst if l%4!=0]
lst42 = []
if len(lst4) > ((H%2) * W//2 + (W%2) * H//2 + (H%2)*(W%2)): jdg = False
elif len(lst4) == 0 and (H%2 == 1 and W%2 == 1):jdg = False 
else:
    lst42 = [l%2 for l in lst4 if l%2!=0]
    if len(lst42) != (H%2) * (W%2): jdg = False

print('Yes' if jdg else 'No')

