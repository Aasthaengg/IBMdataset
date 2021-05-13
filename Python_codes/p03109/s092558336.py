#! python3
#  solve_119_A.py

S = input()
date = S[0:4]+S[5:7]+S[8:10] #yyyymmdd式に変更

tag = 20190430

if int(date) <= 20190430:
    print("Heisei")
else:
    print("TBD")