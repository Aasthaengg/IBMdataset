sentence = input()
new_sent = sentence.split(" ")
acro = ""
for i in new_sent:
  acro += i[0]
print(acro)


