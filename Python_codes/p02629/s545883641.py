# coding: utf-8
# Your code here!

n = int(input())

sub = []
while n > 0:
    if n != 0:
        n -= 1
    sub.append(chr(97 + n % 26))
    n = n // 26

for i in range(len(sub)):
    print(sub[len(sub)-i - 1],end="")
