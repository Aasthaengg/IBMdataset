import sys
kaito = int(0)
line = []
sagasu = str(input().upper())
#tukau = str(sagasu).upper()
while True:
    sonogyo = str(input())
    if sonogyo == "END_OF_TEXT":
        break
    line += sonogyo.upper().split( )
for a in line:
    if a == sagasu:
        kaito = kaito + 1
print(int(kaito))

