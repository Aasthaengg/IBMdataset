
list = {'a':0,'b':25,'c':24,'d':23,'e':22,'f':21,'g':20,'h':19,
         'i': 18,'j':17,'k':16,'l':15,'m':14,'n':13,'o':12,'p':11,
         'q': 10,"r":9,'s':8,'t':7,'u':6,'v':5,'w':4,'x':3,'y':2,'z':1}
list2 = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',
         8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',
         16:'q',17:"r",18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}
list3 = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,
         'i': 8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,
         'q': 16,"r":17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
s = input()

K = int(input())

for i in range(len(s)):
    num = list[s[i]]
    if num <=K:
        s = s[:i] + 'a' + s[i+1:]
        K -= num

if K >0:
    print(s[:-1]+list2[(list3[s[-1]]+K)%26])
else:
    print(s)