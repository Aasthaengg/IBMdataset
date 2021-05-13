s = ""
while True:
    try:
        sent = input()
    except:
        break
    s += sent
    
ch=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
 's','t','u','v','w','x', 'y', 'z']

sl=s.lower()

for c in ch:
    cnt=sl.count(c)
    print("{} : {}".format(c,cnt))