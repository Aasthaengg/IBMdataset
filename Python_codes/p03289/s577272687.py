s = input()
length = len(s)
count = 0
count_large = 0
sep = s[2:length-1]


if s[0] == 'A':
    count += 1

if sep.count('C') == 1:
    count += 1

for i in range(length):
    if s[i].isupper():
        count_large += 1
        
if count_large == 2:
    count += 1

if count == 3:
    print('AC')
else:
    print('WA')
