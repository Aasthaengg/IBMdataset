cookie = (input())
unti = cookie.split()
cookie_1 = int(unti[0])
cookie_2 = int(unti[1])

if cookie_1 % 3 == 0:
   print( "Possible")
elif cookie_2 % 3 == 0:
   print( "Possible")
elif ((cookie_1 + cookie_2) % 3 == 0):
   print( "Possible")
else :
   print( "Impossible")
