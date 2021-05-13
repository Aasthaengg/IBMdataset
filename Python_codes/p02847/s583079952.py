input_date_list = ['SUN','MON','TUE','WED','THU','FRI','SAT' ]
S = input()
today_date_list = ['日','月','火','水','木','金','土']
s1 = input_date_list.index(S)
today_date = (today_date_list[s1])
s2 = 7 - s1
print(s2)