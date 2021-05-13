n = int(raw_input())

ls = map(int,raw_input().split())
mi = min(ls)
ma = max(ls)
su = sum(ls)
print "%d %d %d" % (mi,ma,su)