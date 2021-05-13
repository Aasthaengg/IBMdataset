
while True:
     k = int(input())
     if 1 <= int(k) <= 100:
         break;
     print ('Error Invalid Input for K')
#Check constraint k

while True:
     s = input()
     if 1 <= len(s) <= 100:
         break;
     print ('Error Invalid Input for s')
#Check constraint s

if len(s) > k:
    print(s[:k] + "...")  #append
else:
    print(s)