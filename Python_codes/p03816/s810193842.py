n,s = int(raw_input()),set(map(int, raw_input().split()))
print len(s) - (1 if (len(s) & 1 == 0) else 0)