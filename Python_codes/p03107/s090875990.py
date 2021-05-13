S=sorted(input())
import bisect

i=bisect.bisect_right(S,'0')
o=len(S)-i
z=i
print(len(S)-abs(o-z))