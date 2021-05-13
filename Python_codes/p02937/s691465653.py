
import sys
import bisect

s = input()
t = input()

existing_alphabets = [[]for _ in range(26)]

for i in range(len(s)):
    existing_alphabets[ord(s[i])-97].append(i)

numbered_t = [0]*len(t)
for i in range(len(t)):
    numbered_t[i] = (ord(t[i])-97)

# confirmation each necessary alphabet exists
all_necessary_alphabets = set()
for i in range(len(t)):
    all_necessary_alphabets.add(numbered_t[i])

for necessary_alphabet in all_necessary_alphabets:
    if len(existing_alphabets[necessary_alphabet])==0:
        print(-1)
        sys.exit()

# counting order process
now = -1
cycled = 0
for i in range(len(numbered_t)):
    existing_alphabet = existing_alphabets[numbered_t[i]]
    can_insert = bisect.bisect_right(existing_alphabet,now)
    if can_insert == len(existing_alphabet):
        can_insert = 0
        cycled += 1
    now = existing_alphabet[can_insert]

ans = len(s) * cycled + now + 1
print(ans)