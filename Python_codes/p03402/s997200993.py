#1. imput
a, b = map(int, input().split())

s = ''

W = '.'
B = '#'
N = '\n'

h = 0

#2. make board(width=100)
#2.1 white
#2.1.1 if a>50
while a>=51:
    s += (B+W)*50 + N
    s += B*100 + N
    h += 2
    
    a -= 50

#2.1.2 after a<= 50
a -= 1

s += B*100 + N
s += (B+W)*a + (B+B)*(50-a) + N
s += B*100 + N
h += 3

# 2.2 black
s += W*100 + N
h += 1

# 2,2,1 if b>50
while b >= 51:
    s += (B+W)*50 + N
    s += W*100 + N
    h += 2
    
    b -= 50

# 2.2.2 after b<=50
b -= 1
    
s += (B+W)*b + (W+W)*(50-b) + N
h += 1

#3. output    
print(h, 100)
print(s)