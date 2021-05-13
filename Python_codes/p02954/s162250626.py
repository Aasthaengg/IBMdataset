s = input() + 'R'
a = [0] * (len(s) - 1);

prechar = 'R'
prepos = 0
odd = 0
even = 0
for i in range(len(s)):
    if prechar == 'R':
        if s[i] == 'L':
            prechar = 'L'
            prepos = i-1
    else:
        if s[i] == 'R':
            if (i - prepos) % 2 == 1:
                odd, even = even, odd
            a[prepos] = odd
            a[prepos+1] = even
            prechar = 'R'
            odd = 0
            even = 0
    odd, even = even, odd + 1
    #print(odd+even)

#print(a)
for i in range(len(s) - 1):
    if i != len(s) - 2:
        print(a[i], end=" ")
    else:
        print(a[i])

