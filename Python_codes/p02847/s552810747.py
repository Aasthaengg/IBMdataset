arr=['MON','TUE','WED','THU','FRI','SAT','SUN']
s=input()
if s=='SUN':
    print (7)
else:
    k=arr.index(s)
    print (6-k)