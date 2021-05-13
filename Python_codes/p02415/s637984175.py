words = input()
_words = ""
for case in words:
  if case != case.upper():
    case = case.upper()
  elif case != case.lower():
    case = case.lower()
  _words += case
print (_words)