n = int(input())
s_l = [input() for _ in range(n)]

count = 0
xxxa = 0
bxxx = 0
bxxxa = 0
for st in s_l:
    if 'AB' in st:
        count += st.count('AB')
    if st.endswith('A'):
        if st.startswith('B'):
            bxxxa += 1
        else:
            xxxa += 1
    elif st.startswith('B'):
        bxxx += 1

if max(xxxa,bxxx) == 0:
    count += max(0, bxxxa - 1)
    print(count)
    exit()

while min(xxxa,bxxx,bxxxa) > 0:
    xxxa -= 1
    bxxx -= 1
    bxxxa -= 1
    count += 2
count += bxxxa
count += min(xxxa,bxxx)
print(count)