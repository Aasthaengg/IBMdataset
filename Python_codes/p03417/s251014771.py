w, h = map(int, input().split())
 
count = 0
 
if w == h == 1:
    count = 1
elif w == 1 or h == 1:
    count = max(w,h)-2
else:
    count = (w - 2) * (h - 2)
    
print(count)