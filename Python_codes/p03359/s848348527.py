from sys import stdin
A, B = [int(x) for x in stdin.readline().rstrip().split()] #空白区切り
if B<A:
    A-=1;
print(A)
