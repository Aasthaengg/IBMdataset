print "\n".join(s for s in map(lambda x:x[0]+x[1]==x[2] and 'YES' or 'NO', [sorted(int(x)**2 for x in raw_input().split(' ')) for i in range(int(raw_input()))]))