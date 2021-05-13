
import sys

read= sys.stdin.buffer.read
l= list(map(int, open(0).read().split()))

if (max(l[:5])-min(l[:5]))>l[5]:print(':(')
else:print('Yay!')