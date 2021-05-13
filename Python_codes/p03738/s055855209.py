from sys import stdin, stdout 

a = int(stdin.readline()) 
b = int(stdin.readline())

if a > b:
    stdout.write(str('GREATER'))
elif a < b:
    stdout.write(str('LESS'))
else:
    stdout.write(str('EQUAL')) 