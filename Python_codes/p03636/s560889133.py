import sys 

line = sys.stdin.read()
line = line.strip()
start = line[0]
end = line[-1]
print('%s%d%s'%(start, len(line) - 2, end))
  
