n=int(input())
hennsai=100000
for i in range(n):
    hennsai=int(hennsai*1.05)
    if hennsai % 1000>0:
        hennsai=(hennsai - hennsai % 1000) + 1000
print(hennsai)

    
