import sys
count = 0
w = ""
w = raw_input()
while 1 :
    adding = map(str,raw_input().split())
    for i in adding:
          if i == 'END_OF_TEXT':
              print count
              sys.exit()
          if i.lower() == w:
              count += 1