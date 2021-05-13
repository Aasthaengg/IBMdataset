a = int(raw_input())
b = int(raw_input())
h = int(raw_input())
s = max(a,b) * h
s-= (max(a,b) - min(a,b))/2.0*h
print int(s)