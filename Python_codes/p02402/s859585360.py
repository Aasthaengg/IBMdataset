raw_input()
args = map(int, raw_input().split(" "))
print " ".join(map(str, [min(args), max(args), sum(args)]))