FAST_IO = 0
if FAST_IO:
    import io, sys, atexit
    rr = iter(sys.stdin.read().splitlines()).next
    sys.stdout = _OUTPUT_BUFFER = io.BytesIO()

    @atexit.register
    def write():
        sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
else:
    rr = raw_input
rri = lambda: int(rr())
rrm = lambda: map(int, rr().split())
rrmm = lambda n: [rrm() for _ in xrange(n)]

####
MOD = 10**9 + 7
YES, NO, IMP = "YES", "NO", "IMPOSSIBLE"
from collections import defaultdict as ddic

a,b,c,d = rrm()
cand = [a*c,a*d,b*c,b*d]
print max(cand)
