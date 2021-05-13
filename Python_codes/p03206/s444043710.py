import sys
D = int(input())
D -= 25
sys.stdout.write('Christmas')
while D<0:
    sys.stdout.write(' Eve')
    D += 1