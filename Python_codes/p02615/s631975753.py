n  = int(input())
ai = list(reversed(sorted(map(int, input().split()))))

added   = 2
mins    = [ ai[1], ai[1] ]
comfort = ai[0]

def double(xs):
    for x in xs:
        yield x
        yield x

while added < len(ai):
    pick = mins[ : len(ai) - added ]
    comfort += sum(pick)
    mins = list(double(ai[ added : added + len(pick) ]))
    added += len(pick)

print(comfort)

# 7 6 5 4 3 2 1 0

# (0) 7
# (_ + 7 * 1) 7 6
# (_ + 6 * 2) 7 5 6 4
# (_ + 5 * 2 + 4 * 2) 7 3 5 2 6 1 4 0